start Python3
`$ python3`

end session
`ctrl + D`

create a project
`$ mkdir NameOfApp`

create virtual environment
`$ cd NameOfApp`
`$ virtualenv ($NameOfApp)Venv`

activate virtual environment
`$ source ($NameOfApp)Venv/bin/activate`

install package
(NaeOfAppVenv) `$ pip install Django`

turn off virtual environment
`$ deactivate`

freeze requirements
`$ pip freeze > requirements.txt`

import from requirements.txt
`$ pip install -r requirements.txt`
