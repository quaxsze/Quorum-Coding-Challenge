# Quorum-Coding-Challenge

The commit of this project follow the [gitmoji](https://gitmoji.dev/) convention for better readability.

#### Setup the project
Install project's dependancies:\
`poetry install`

Enter project's env:\
`poetry shell`

#### Create and fill the sqlite database with CSV files 
(the order of execution is important to respect the foreign keys assignment)
```
python manage.py migrate
python manage.py import_legislator_csv legislators.csv
python manage.py import_bill_csv bills.csv
python manage.py import_vote_csv votes.csv
python manage.py import_vote_result_csv vote_results.csv
```

#### Run the dev server
`python manage.py runserver`

#### Available endpoints
`/legislative/legislator/<megislator_id>/` : Returns for a given legislator, the number of bills the legislator did support and oppose.\
`/legislative/bill/<bill_id>/` : Returns for a given bill, the number of legislators that supported the bill and the number that opposed it.

#### Tests
Run unit tests:\
`python manage.py tests`