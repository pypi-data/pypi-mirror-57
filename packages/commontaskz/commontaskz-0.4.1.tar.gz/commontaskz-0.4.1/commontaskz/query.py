_B='error'
_A=None
import requests,logging
from prefect import task,Task
from prefect.utilities.tasks import defaults_from_attrs
from prefect.client import Secret
from prefect.utilities.notifications import slack_notifier
from prefect.engine.state import Failed
def camel_case(words):
	A=words
	if A:return A.title().replace(' ','')
	return''
class Query(Task):
	def __init__(A,name=_A,url=_A,key=_A):A.name=name;A.url=url;A.key=key;A.log_prefix=A.build_log_prefix();super().__init__()
	def query(B,url):
		A=url
		if _B in A:return A
		logging.debug('{}: url {}'.format(B.log_prefix,A))
		try:C=requests.get(url=A,params={},headers={'Authorization':B.key});return C
		except:return B.error('failed to query with url {}'.format(A))
	def process(B,response):
		A=response
		if _B in A:return A
		try:
			if A.status_code!=200:return B.error('response code was {}'.format(A.status_code))
			C=A.json()
			if not C or C=={}:return B.error('json is empty')
			return C
		except:return B.error('bad response')
	def error(B,msg):A='{}: {}'.format(B.log_prefix,msg);logging.error(A);return{_B:A}
	def build_log_prefix(A):return 'Query{}'.format(camel_case(A.name))
	@defaults_from_attrs('url')
	def run(self,data,url=_A):A=self;B=A.prep(url,data);C=A.query(B);D=A.process(C);return D