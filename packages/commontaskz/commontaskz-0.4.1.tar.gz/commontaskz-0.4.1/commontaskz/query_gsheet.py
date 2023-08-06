_A=None
import requests,logging
from prefect.utilities.tasks import defaults_from_attrs
from .query import Query
class QueryGSheet(Query):
	'\n    Base class for querying CA\n    '
	def __init__(A,key=_A,url=_A,a_range=_A,sheet_id=_A,sheet_name=_A):super().__init__(key,url);A.name='GSheet';A.key=key;A.url=url;A.a_range=a_range;A.sheet_id=sheet_id;A.sheet_name=sheet_name;A.log_prefix=A.build_log_prefix()
	def prep(B,url,key,a_range,sheet_id,sheet_name):A=url;A='{url}/{sheet_id}/values/{sheet_name}!{a_range}?key={key}'.format(url=A,sheet_id=sheet_id,sheet_name=sheet_name,a_range=a_range,key=key);return A
	def query(A,url):return requests.get(url,params={},headers={})
	def post_process(C,result):
		F='values';B=result;A=[]
		if F not in B:return[]
		D=B[F]
		for E in D:A+=E
		logging.debug('{}: {} companies returned'.format(C.log_prefix,len(A)));A=[B for B in A if B!=''];return A
	@defaults_from_attrs('url','key','a_range','sheet_id','sheet_name')
	def run(self,url=_A,key=_A,a_range=_A,sheet_id=_A,sheet_name=_A):A=self;B=A.prep(url,key,a_range,sheet_id,sheet_name);C=A.query(B);D=A.process(C);E=A.post_process(D);return E