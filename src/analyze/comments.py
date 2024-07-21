import utils.infos as infos
from typing import Dict, Any, List

def get_comments(data: Dict[str, Any]) -> int:
	"""
	Get the number of comments.
	"""
	comment_list: List[Any] = data.get("Comment", {}).get("Comments", {}).get("CommentsList", {})
	comments: int = len(comment_list)
	return comments