# ==========================================
# Name:   python-papermill-jupyter.py
# ==========================================
'''
References:
* Papermill documentation, execute via Python API.  https://papermill.readthedocs.io/en/latest/usage-execute.html
* Towards Data Science, introduction to papermill.  https://towardsdatascience.com/introduction-to-papermill-2c61f66bea30
* Github papermill.  https://github.com/nteract/papermill
'''

import papermill as pm

pm.execute_notebook(
   'path/to/input.ipynb',
   'path/to/output.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)
