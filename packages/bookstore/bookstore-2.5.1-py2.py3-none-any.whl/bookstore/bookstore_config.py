"""Configuration settings for bookstore."""
import logging
from pathlib import Path

from traitlets import Integer, Unicode, Bool
from traitlets.config import LoggingConfigurable

log = logging.getLogger('bookstore_config')


class BookstoreSettings(LoggingConfigurable):
    """Configuration for archival and publishing.

    Settings include storage directory locations, S3 authentication,
    additional S3 settings, and Bookstore resources.

    S3 authentication settings can be set, or they can be left unset when
    IAM is used.

    Like the Jupyter notebook, bookstore uses traitlets to handle
    configuration, loading from files or CLI.

    Attributes
    ----------
    workspace_prefix : str(``workspace``)
                       Directory to use for user workspace storage
    published_prefix : str(``published``)
                       Directory to use for published notebook storage
    s3_access_key_id : str, optional
                       Environment variable ``JPYNB_S3_ACCESS_KEY_ID``
    s3_secret_access_key : str, optional
                       Environment variable ``JPYNB_S3_SECRET_ACCESS_KEY``
    s3_endpoint_url : str(``"https://s3.amazonaws.com"``)
                       Environment variable ``JPYNB_S3_ENDPOINT_URL``
    s3_region_name : str(``"us-east-1"``)
                       Environment variable ``JPYNB_S3_REGION_NAME``
    s3_bucket : str(``""``)
                Bucket name, environment variable ``JPYNB_S3_BUCKET``
    max_threads : int(``16``)
                  Maximum threads from the threadpool available for S3 read/writes
    enable_s3_cloning : bool(``True``)
                        Enable cloning from s3.
    fs_cloning_basedir : str(``"/Users/jupyter"``)
                        Absolute path to base directory used to clone from the local file system
                  
    """

    workspace_prefix = Unicode("workspace", help="Prefix for the live workspace notebooks").tag(
        config=True
    )
    published_prefix = Unicode("published", help="Prefix for published notebooks").tag(config=True)
    enable_s3_cloning = Bool(True, help="Enable cloning from s3.").tag(config=True)

    s3_access_key_id = Unicode(
        help="S3/AWS access key ID", allow_none=True, default_value=None
    ).tag(config=True, env="JPYNB_S3_ACCESS_KEY_ID")
    s3_secret_access_key = Unicode(
        help="S3/AWS secret access key", allow_none=True, default_value=None
    ).tag(config=True, env="JPYNB_S3_SECRET_ACCESS_KEY")

    s3_endpoint_url = Unicode("https://s3.amazonaws.com", help="S3 endpoint URL").tag(
        config=True, env="JPYNB_S3_ENDPOINT_URL"
    )
    s3_region_name = Unicode("us-east-1", help="Region name").tag(
        config=True, env="JPYNB_S3_REGION_NAME"
    )
    s3_bucket = Unicode("", help="Bucket name to store notebooks").tag(
        config=True, env="JPYNB_S3_BUCKET"
    )

    max_threads = Integer(
        16, help="Maximum number of threads for the threadpool allocated for S3 read/writes"
    ).tag(config=True)

    fs_cloning_basedir = Unicode(
        "", help=("Absolute path to base directory used to clone from the local file system")
    ).tag(config=True)


def validate_bookstore(settings: BookstoreSettings):
    """Check that settings exist.

    Parameters
    ----------
    settings : bookstore.bookstore_config.BookstoreSettings
               Instantiated settings object to be validated.

    Returns
    -------
    validation_checks : dict
        Statements about whether features are validly configured and available
    """
    general_settings = [settings.s3_bucket != "", settings.s3_endpoint_url != ""]
    archive_settings = [*general_settings, settings.workspace_prefix != ""]
    published_settings = [*general_settings, settings.published_prefix != ""]
    s3_cloning_settings = [settings.enable_s3_cloning]
    fs_cloning_settings = [Path(settings.fs_cloning_basedir).is_absolute()]

    validation_checks = {
        "bookstore_valid": all(general_settings),
        "archive_valid": all(archive_settings),
        "publish_valid": all(published_settings),
        "s3_clone_valid": all(s3_cloning_settings),
        "fs_clone_valid": all(fs_cloning_settings),
    }
    if not validation_checks["fs_clone_valid"] and settings.fs_cloning_basedir != "":
        log.info(
            f"{settings.fs_cloning_basedir} is not an absolute path, file system cloning will be disabled."
        )

    return validation_checks
