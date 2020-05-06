# Takathon
Takathon is a language focused on QA and unit testing.

## Design Goals
The main goal is similiar to [Specification by example](https://en.wikipedia.org/wiki/Specification_by_example) goals, namely to merge tests, documentation and type system into one thing called specification. Specification describes a chunk of code (e.g. function).

This approach has plenty of benefits:
* Declarative and readable tests
* Documentation and usage examples generated directly from specification
* Helpful error messages
* Easier debugging
* Testing in real time
* Native TDD support

## Usage
Testing factorial function for several arguments and expected exception:
```
def factorial(n):
    """
    spec:
        title: Factorial
        domain -1:
            title: Should be incalculable for negative values
            description: Function raises proper exception when called with negative value
            throws ValueError('factorial() not defined for negative values')
        domain 0:
            title: Should return 1 on boundary
            description: Function should return 0 when called with 0
            results 1
        domain 1: results 1
        domain 3: results 6
        domain 4: results 24
        domain 5: results 120
    """
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n == 0:
        return 1
    return n * factorial(n - 1)
```
Other examples are located in [examples/](examples) directory. To test a specific file you can use `takathon <file-name>` command inside docker container

## Development
Preferred way is to use docker for development. To run the tool install docker-compose and type `docker-compose run --rm app`.

### Testing
Run `python src/takathon examples` to test the code against examples. 
