from prefect.utilities.tasks import defaults_from_attrs
from .query import Query
class QueryDatasysCompany(Query):
	def __init__(A,key,url=None):super().__init__(key,url);A.name='Datasys';A.url=url;A.key=key;A.log_prefix=A.build_log_prefix()
	def prep(B,url,datasys_id):
		A=datasys_id
		if'error'in A:return A
		return '{}/repository/company/{}?trace=false'.format(url,A)
	@defaults_from_attrs('url')
	def run(self,data,url=None):A=self;B=A.prep(url,data);C=A.query(B);D=A.process(C);return D