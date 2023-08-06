import logging
import importlib

from awswrangler.__version__ import __title__, __description__, __version__  # noqa
from awswrangler.session import Session  # noqa
from awswrangler.pandas import Pandas  # noqa
from awswrangler.s3 import S3  # noqa
from awswrangler.athena import Athena  # noqa
from awswrangler.cloudwatchlogs import CloudWatchLogs  # noqa
from awswrangler.glue import Glue  # noqa
from awswrangler.redshift import Redshift  # noqa
from awswrangler.emr import EMR  # noqa
import awswrangler.utils  # noqa
import awswrangler.data_types  # noqa

if importlib.util.find_spec("pyspark"):  # type: ignore
    from awswrangler.spark import Spark  # noqa

logging.getLogger("awswrangler").addHandler(logging.NullHandler())
