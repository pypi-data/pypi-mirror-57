"Main interface for workmailmessageflow service type defs"
import sys
from typing import IO

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
from typing import Union


GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef", {"messageContent": Union[bytes, IO]}
)
