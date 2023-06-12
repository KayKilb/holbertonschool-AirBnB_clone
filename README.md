# AirBnB Clone Project

## Part 1 - command interpreter

### This project will entail:

- Putting in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
- Creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- Creating all classes used for AirBnB (`User`, `State`, `City`, `Place…`) that inherit from `BaseModel`
- Create the first abstracted storage engine of the project: File storage.
- Create all unittests to validate all our classes and storage engine
### How to use it:
1. Start up the console by typing `./console`.
2. Type `help` to see what commands are available.
3. To quit the console, type `Quit` to quit.
### Examples:
```
(hbnb) create BaseModel
7e45fdeb-bfe0-4010-b336-3d9edb454e04
(hbnb) all BaseModel
[[BaseModel] (43145a16-c555-4ac3-9366-639decb8e3cb) {'id': '43145a16-c555-4ac3-9366-639decb8e3cb', 'created_at': datetime.datetime(2023, 6, 12, 16, 10, 16, 539262), 'updated_at': datetime.datetime(2023, 6, 12, 16, 10, 16, 539262)}, [BaseModel] (7e45fdeb-bfe0-4010-b336-3d9edb454e04) {'id': '7e45fdeb-bfe0-4010-b336-3d9edb454e04', 'created_at': datetime.datetime(2023, 6, 12, 16, 12, 39, 539167), 'updated_at': datetime.datetime(2023, 6, 12, 16, 12, 39, 539167)}]

```
### Authors:
* Rob Hollis <6123@holbertonstudents.com>
* Kaylene Kilbourn <6158@holbertonstudents.com>