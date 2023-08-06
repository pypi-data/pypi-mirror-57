from enum import Enum
import os.path
import six
import io
from base64 import b64encode
from tempfile import NamedTemporaryFile
import warnings

try:
    import collections.abc as abc
except ImportError:
    import collections as abc

import numpy as np

from descarteslabs.common.property_filtering import GenericProperties
from descarteslabs.client.services.service import ThirdPartyService

from .catalog_base import DocumentState, check_deleted
from .named_catalog_base import NamedCatalogObject
from .attributes import (
    Attribute,
    EnumAttribute,
    GeometryAttribute,
    Timestamp,
    ListAttribute,
    File,
)

properties = GenericProperties()


class StorageState(str, Enum):
    """The storage state for an image.

    Attributes
    ----------
    AVAILABLE : enum
        The image data has been uploaded and can be rastered.
    REMOTE : enum
        The image data is has not been uploaded, but its location is known.
    """

    AVAILABLE = "available"
    REMOTE = "remote"


class Image(NamedCatalogObject):
    """An image with raster data.

    Parameters
    ----------
    kwargs : dict
        With the exception of readonly attributes
        (:py:attr:`~descarteslabs.catalog.CatalogObject.created`,
        :py:attr:`~descarteslabs.catalog.CatalogObject.modified`), any
        (inherited) attribute listed below can also be used as a keyword argument.

    Inheritance
    -----------
    For inherited parameters, methods, attributes, and properties, please refer to the
    base classes:

    * :py:class:`descarteslabs.catalog.NamedCatalogObject`
    * :py:class:`descarteslabs.catalog.CatalogObject`

    |

    Attributes
    ----------
    geometry : shapely.geometry.base.BaseGeometry, geojson-like
        Required: Geometry representing the image coverage.
        *Filterable*
        (use :py:meth:`ImageSearch.intersects`)
    cs_code : str
        The coordinate reference system used by the image as an EPSG or ESRI code,
        e.g. ``"EPSG:4326"``. One of `cs_code` and `projection` is required. If
        both are set and disagree, `cs_code` takes precedence.
    projection : str
        The spatial reference system used by the image either as a proj.4 string or
        a WKT string. One of `cs_dode` and `projection` is required.
        If both are set and disagree, `cs_code` takes precedence.
    geotrans : `list` of six `float` elements
        GDAL-style `geotransform matrix <https://gdal.org/user/raster_data_model.html#affine-geotransform>`_
        that transforms pixel coordinates into the spatial reference system defined by the `cs_code`
        or `projection` attributes
    x_pixels : int
        X dimension of the image in pixels
    y_pixels : int
        Y dimension of the image in pixels
    acquired : str, datetime-like
        Required: Timestamp when the image was captured by its sensor or created.
        *Filterable, sortable*.
    acquired_end : str, datetime-like
        Timestamp when the image capture by its sensor was completed.
        *Filterable, sortable*.
    published : str, datetime-like
        Timestamp when the data provider published this image. *Filterable, sortable*.
    storage_state : StorageState
        Required: Storage state of the image; "available" if the data is available
        and can be rastered, "remote" if the data is not currently available.
        *Filterable, sortable*.
    files : list(File)
        The list of files holding data for this image.
    area : float
        Surface are the image covers.
        *Filterable, sortable*.
    azimuth_angle : float
        Sensor azimuth angle in degrees.
        *Filterable, sortable*.
    bits_per_pixel : list(float)
        Average bits of data per pixel per band
    bright_fraction : float
        Fraction of the image that has reflectance greater than .4 in the blue band.
        *Filterable, sortable*.
    cloud_fraction : float
        Fraction of pixels which are obscured by clouds.
        *Filterable, sortable*.
    alt_cloud_fraction : float
        Fraction of pixels which are obscured by clouds, as per an alternative
        algorithm.
        *Filterable, sortable*.
    processing_pipeline_id : str
        Identifier for the pipeline that processed this image from raw data.
        *Filterable, sortable*.
    fill_fraction : float
        Fraction of this image which has data.
        *Filterable, sortable*.
    incidence_angle : float
        Sensor incidence angle in degrees.
        *Filterable, sortable*.
    reflectance_scale : list(float)
        Scale factors converting TOA radiances to TOA reflectances
    roll_angle : float
        Applicable only to Landsat 8, roll angle in degrees.
        *Filterable, sortable*.
    solar_azimuth_angle : float
        Solar azimuth angle at capture time.
        *Filterable, sortable*.
    solar_elevation_angle : float
        Solar elevation angle at capture time.
        *Filterable, sortable*.
    view_angle : float
        Sensor view angle in degrees.
        *Filterable, sortable*.
    satellite_id : str
        Id of the capturing satellite/sensor among a constellation of many satellites.
        *Filterable, sortable*.
    provider_id : str
        Id that uniquely ties this image to an entity as understood by the data
        provider.
        *Filterable, sortable*.
    provider_url : str
        An external (http) URL that has more details about the image
    preview_url : str
        An external (http) URL to an image that could be inlined in a UI to show a
        preview for the image
    preview_file : str
        A GCS URL (gs://) with a georeferenced image that can be used to raster the
        image in a preview context, generally low resolution. It should be a 3-band
        (RBG) or a 4-band (RGBA) image suitable for visual preview. (It's not
        expected to conform to the bands of the products.)

    """

    _doc_type = "image"
    _url = "/images"
    _default_includes = ["product"]
    _gcs_upload_service = ThirdPartyService()

    # Geo referencing
    geometry = GeometryAttribute()
    cs_code = Attribute()
    projection = Attribute()
    geotrans = Attribute()
    x_pixels = Attribute()
    y_pixels = Attribute()

    # Time dimensions
    acquired = Timestamp()
    acquired_end = Timestamp()
    published = Timestamp()

    # Stored files
    storage_state = EnumAttribute(StorageState)
    files = ListAttribute(File)

    # Image properties
    area = Attribute()
    azimuth_angle = Attribute()
    bits_per_pixel = ListAttribute(Attribute)
    bright_fraction = Attribute()
    cloud_fraction = Attribute()
    alt_cloud_fraction = Attribute()
    processing_pipeline_id = Attribute()
    fill_fraction = Attribute()
    incidence_angle = Attribute()
    reflectance_scale = ListAttribute(Attribute)
    roll_angle = Attribute()
    solar_azimuth_angle = Attribute()
    solar_elevation_angle = Attribute()
    view_angle = Attribute()
    satellite_id = Attribute()

    # Provider info
    provider_id = Attribute()
    provider_url = Attribute()
    preview_url = Attribute()
    preview_file = Attribute()

    @classmethod
    def search(cls, client=None):
        """A search query for all images.

        Return an `ImageSearch` instance for searching images in the Descartes Labs
        catalog.  This instance extends the
        :py:class:`~descarteslabs.catalog.search.Search` class with the
        :py:meth:`~descarteslabs.catalog.search.ImageSearch.summary` and
        :py:meth:`~descarteslabs.catalog.search.ImageSearch.summary_interval` methods
        which return summary statistics about the images that match the search query.

        Parameters
        ----------
        client : :class:`CatalogClient`, optional
            A `CatalogClient` instance to use for requests to the Descartes Labs
            catalog.

        Returns
        -------
        :class:`~descarteslabs.catalog.search.ImageSearch`
            An instance of the `ImageSearch` class

        Example
        -------
        >>> search = Image.search().limit(10)
        >>> for result in search:
                print(result.name)

        """
        from .search import ImageSearch

        return ImageSearch(cls, client=client)

    @check_deleted
    def upload(self, files, upload_options=None):
        """Uploads imagery from a file (or files).

        Uploads imagery from a file (or files) in GeoTIFF or JP2 format to be ingested
        as an Image.

        Parameters
        ----------
        files : str or io.IOBase or list of same
            File or files to be uploaded. Can be string with path to the file
            in the local filesystem, or an opened file (``io.IOBase``), or an iterable
            of either of these when multiple files make up the image.
        upload_options : :py:class:`ImageUploadOptions`, optional
            Optional control of the upload process.

        Raises
        ------
        ValueError
            If any improper arguments are supplied.
        DeletedObjectError
            If this image was deleted.

        Returns
        -------
        :py:class:`ImageUpload`
            An :py:class:`ImageUpload` instance which can be used to check the status or
            wait on the asynchronous upload process to complete.
        """
        from .image_upload import ImageUploadType, ImageUploadOptions

        if not self.id:
            raise ValueError("id field required")
        if not self.acquired:
            raise ValueError("acquired field required")

        if self.product.state != DocumentState.SAVED:
            raise ValueError(
                "Product {} has not been saved. Please save before uploading images".format(
                    self.product_id
                )
            )

        # convert file to a list, validating and extracting file names
        if isinstance(files, six.string_types) or isinstance(files, io.IOBase):
            files = [files]
        elif not isinstance(files, abc.Iterable):
            raise ValueError(
                "Invalid files value: must be string, IOBase, or iterable of the same"
            )
        filenames = []
        for f in files:
            if isinstance(f, six.string_types):
                filenames.append(os.path.basename(f))
            elif isinstance(f, io.IOBase):
                filenames.append(os.path.basename(f.name))
            else:
                raise ValueError(
                    "Invalid files value: must be string, IOBase, or iterable of the same"
                )
        if not filenames:
            raise ValueError("Invalid files value has zero length")

        if not upload_options:
            upload_options = ImageUploadOptions()

        upload_options.upload_type = ImageUploadType.FILE
        upload_options.image_files = filenames

        # Note that this uses a V1 code path
        return self._do_upload(files, upload_options)

    @check_deleted
    def upload_ndarray(
        self,
        ndarray,
        upload_options=None,
        raster_meta=None,
        overviews=None,
        overview_resampler=None,
    ):
        """Uploads imagery from an ndarray to be ingested as an Image.

        Note that one of the spatial reference attributes (`cs_dode` and
        `projection`), and/or `geotrans` parameters can be
        specified explicitly in the image, or the `raster_meta` parameter can be
        specified.  Likewise, `overviews` and `overview_resampler` can be
        specified explicitly, or via the `upload_options` parameter.


        Parameters
        ----------
        ndarray : np.array
            A numpy array with image data, either with 2 dimensions of shape
            ``(x, y)`` for a single band or with 3 dimensions of shape
            ``(band, x, y)`` for any number of bands.  If providing a 3d array
            the first dimension must index the bands.  The ``dtype`` of the array must
            also be one of the following:
            [``uint8``, ``int8``, ``uint16``, ``int16``, ``uint32``, ``int32``,
            ``float32``, ``float64``]
        upload_options : :py:class:`ImageUploadOptions`, optional
            Optional control of the upload process.
        raster_meta : dict, optional
            Metadata returned from the :meth:`Raster.ndarray()
            <descarteslabs.client.services.raster.Raster.ndarray>` request which
            generated the initial data for the `ndarray` being uploaded.  Specifying
            `image.geotrans` and one of the spatial reference attributes
            (`image.cs_code` and `image.projection`) is unnecessary
            in this case, but if either of those fields is set in the `image`
            parameter then it will take precedence over the value in `raster_meta`.
        overviews : list(int), optional
            Overview resolution magnification factors e.g.  [2, 4] would make two
            overviews at 2x and 4x the native resolution.  Maximum number of overviews
            allowed is 16.  Can also be set in the `upload_options` parameter.
        overview_resampler : str, optional
            Resampler algorithm to use when building overviews.  Controls how pixels
            are combined to make lower res pixels in overviews.  Allowed resampler
            algorithms are: [``nearest``, ``average``, ``gauss``, ``cubic``,
            ``cubicspline``, ``lanczos``, ``average_mp``, ``average_magphase``,
            ``mode``].  Can also be set in the `upload_options` parameter.

        Raises
        ------
        ValueError
            If any improper arguments are supplied.
        DeletedObjectError
            If this image was deleted.

        Returns
        -------
        :py:class:`ImageUpload`
            An :py:class:`ImageUpload` instance which can be used to check the status or
            wait on the asynchronous upload process to complete.
        """
        from .image_upload import ImageUploadType, ImageUploadOptions

        if not self.id:
            raise ValueError("id field required")
        if not self.acquired:
            raise ValueError("acquired field required")

        if self.product.state != DocumentState.SAVED:
            raise ValueError(
                "Product {} has not been saved. Please save before uploading images".format(
                    self.product_id
                )
            )

        if len(ndarray.shape) not in (2, 3):
            raise ValueError(
                "The array must have 2 dimensions (shape '(x, y)') or 3 dimensions with the band "
                "axis in the first dimension (shape '(band, x, y)'). The given array has shape "
                "'{}' instead.".format(ndarray.shape)
            )

        if len(ndarray.shape) == 3:
            scale_factor = 5
            scaled_band_dim = ndarray.shape[0] * scale_factor
            if scaled_band_dim > ndarray.shape[1] or scaled_band_dim > ndarray.shape[2]:
                warnings.warn(
                    "The shape '{}' of the given 3d-array looks like it might not have the band "
                    "axis as the first dimension. Verify that your array conforms to the shape "
                    "'(band, x, y)'".format(ndarray.shape)
                )
            # v1 ingest expects (X,Y,bands)
            ndarray = np.moveaxis(ndarray, 0, -1)

        # default to raster_meta fields if not explicitly provided
        if raster_meta:
            if not self.geotrans:
                self.geotrans = raster_meta.get("geoTransform")
            if not self.cs_code and not self.projection:
                # doesn't yet exist!
                self.projection = raster_meta.get("coordinateSystem", {}).get("proj4")

        if not self.geotrans:
            raise ValueError("geotrans field or raster_meta parameter is required")
        if not self.cs_code and not self.projection:
            raise ValueError(
                "cs_code or projection field is required if "
                + "raster_meta parameter is not given"
            )

        if not upload_options:
            upload_options = ImageUploadOptions()
        upload_options.upload_type = ImageUploadType.NDARRAY
        if overviews:
            upload_options.overviews = overviews
        if overview_resampler:
            upload_options.overview_resampler = overview_resampler

        with NamedTemporaryFile(delete=False) as tmp:
            try:
                np.save(tmp, ndarray, allow_pickle=False)

                # From tempfile docs:
                # Whether the name can be used to open the file a second time,
                # while the named temporary file is still open, varies across
                # platforms (it can be so used on Unix; it cannot on Windows
                # NT or later)
                # We close the underlying file object so _do_upload can open
                # the path again in a cross platform compatible way.
                # Cleanup is manual in the finally block.
                tmp.close()
                upload_options.image_files = [os.path.basename(tmp.name)]
                return self._do_upload([tmp.name], upload_options)
            finally:
                os.unlink(tmp.name)

    def image_uploads(self):
        """A search query for all uploads for this image created by this user.

        Returns
        -------
        :py:class:`~descarteslabs.catalog.search.Search`
            A :py:class:`~descarteslabs.catalog.search.Search` instance configured to
            find all uploads for this image.
        """
        from .image_upload import ImageUpload

        return ImageUpload.search(client=self._client).filter(
            (properties.product_id == self.product_id)
            & (properties.image_id == self.id)
        )

    def _do_upload(self, files, upload_options):
        # This uses the existing V1 code path for uploading images

        from .image_upload import ImageUpload, ImageUploadType, ImageUploadStatus

        # With the new ingest, we will not specify id here and ImageUpload
        # will default to a uuid4. But to keep the old ingest happy,
        # we need to use a specially encoded id that can be decoded by
        # the service to search the tasks. The use of the last filename
        # ensures we track the one task which will actually perform the ingest.
        upload_id = "{}:{}{}".format(
            b64encode(self.product_id.encode("utf-8")).decode("utf-8"),
            os.path.basename(files[-1]),
            ".tif"
            if upload_options.upload_type == ImageUploadType.NDARRAY
            and not files[-1].endswith(".tif")
            else "",
        )
        upload = ImageUpload(
            id=upload_id,
            client=self._client,
            image=self,
            image_upload_options=upload_options,
        )

        upload.save()

        for file, upload_url in zip(files, upload.resumable_urls):
            if isinstance(file, io.IOBase):
                if "b" not in file.mode:
                    file.close()
                    file = io.open(file.name, "rb")
                f = file
            else:
                f = io.open(file, "rb")

            try:
                self._gcs_upload_service.session.put(upload_url, data=f)
            finally:
                f.close()

        upload.status = ImageUploadStatus.PENDING
        upload.save()

        return upload
