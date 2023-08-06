"""Additional exceptions for working with automated tests."""

__all__ = [
    'BrokenTestException',
    'ExcludeTestException',
    'InvalidTestConfigurationException',
    'IrrelevantTestException',
    'TransientTestError',
]


class RichSkipTestException(Exception):
    """Base class for all errors that cause the test to be skipped.
    
    Ideally, the base class would be unittest.SkipTest (or, even better,
    nose.plugins.skip.SkipTest so that it works on all Python versions). This
    way our rich errors would be treated as Skip's if they are not specially
    handled.
    
    However, the default error handling in unittest.TestCase (which is also
    used by Nose) treats SkipTest as a special case (rather than a generic
    error), and strips out all of the exception information apart from the
    message.
    
    Therefore, unless we commit to a rewrite of TestCase.run within Nose, or
    implement some deep magic with __str__, we are reduced to maintaining a
    separate exception hierarchy.
    """
    pass


class BrokenTestException(RichSkipTestException):
    """Skip a test because it is known to be broken.
    
    This avoids constantly re-running tests that are known to fail or cause an
    error, yet allows us to still mark them as failures.
    
    In a perfect Test Driven Development world, all broken tests would be
    fixed immediately by the developer that caused them to break.
    
    However, test frameworks are not necessarily used in a perfect TDD world
    (for instance, consider a situation where tests are being written against
    an existing legacy codebase), so pragmatically we need some process to
    manage the broken tests.
    
    Some example scenarios:
     * The development team decide that the defect exposed by the test can be
        tolerated in the short-term, but will allocate resources to fix it in
        the long-term.
     * It is not known how to fix the defect exposed by the test.
     * The defect exposed by the test is caused by a third party product.
     * The defect exposed by the test cannot be fixed without making
        incompatible changes to the product's external API (and these changes
        need to be carefully managed).
    
    This differs from the standard unittest.expectedFailure decorator in that
    it does not attempt to run the test. It is also more flexible
    (expectedFailure can only be applied to functions as a decorator), and
    there is support for it in Nose.
    
    It is expected that each broken test will have an associated defect item
    in the project's issue tracker. This must be included in the exception
    as a separate field.
    """
    def __init__(self, item_number, reason):
        super(BrokenTestException, self).__init__(reason)
        
        self.item_number = item_number
        self.reason = reason
    
    def __repr__(self):
        return "%s(%s, '%s')" % (self.__class__.__name__, repr(self.item_number), self.reason)
    
    def __str__(self):
        return "Broken Test: %s (defect #%s)" % (self.reason, self.item_number)


class ExcludeTestException(RichSkipTestException):
    """Skip a test because the user specifically excluded it from the current
    test run.
    
    This differs from the standard unittest.SkipTest exception in that it is
    specifically intended for exclusions specified at test-run-time, whereas
    SkipTest has a very general meaning and implies nothing about the reason
    for skipping the test.
    
    Note that there may be other ways to exclude unwanted tests (eg. Nose
    provides several ways to specify which functions should be considered as
    tests).
    """
    #TODO this description and use case is still weak, and wishy washy
    pass


class InvalidTestConfigurationException(RichSkipTestException):
    """Skip a test because the system is not configured correctly.
    
    For example, this might be used when a test fixture cannot be setup because
    important configuration information (such as the database to connect to)
    has not been supplied by the user. 
    
    This situation should be considered a test failure.
    
    @see IrrelevantTestException: Some configuration problems simply mean that
        a test should be skipped because it is not relevant for the current
        system.
    """
    pass


class IrrelevantTestException(RichSkipTestException):
    """Skip a test because it is not relevant for the current system.
    
    For example, this might be used to avoid running a Linux-specific test
    under Microsoft Windows.
    """
    pass


class TransientTestError(RichSkipTestException):
    """A test failed due to a transient error outside the test environment.
    
    For example, this might be used when there is an issue with network
    connectivity, or when a 3rd party webservices server is temporarily
    unavailable.
    """
    pass