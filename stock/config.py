from ssi_fc_data import fc_md_client , model
import plotly.graph_objs as go
import plotly.subplots as sp
import pandas as pd 
from pandas import json_normalize
import requests

auth_type = 'Bearer'
consumerID = 'e236036eebb74c79a956e577eefae726'
consumerSecret = 'a6704fef62be44ff8aac9358a4a87805'

url = 'https://fc-data.ssi.com.vn/'
stream_url = 'https://fc-datahub.ssi.com.vn/'

