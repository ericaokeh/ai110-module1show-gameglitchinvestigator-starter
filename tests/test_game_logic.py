from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# New Tests
def test_parse_guess_valid():
    # Test valid guesses within bounds
    low, high = 1, 100
    valid, parsed_guess, error_message = parse_guess("50", low, high)
    assert valid
    assert parsed_guess == 50
    assert error_message is None

def test_parse_guess_out_of_bounds_low():
    # Test a guess below the lower bound
    low, high = 1, 100
    valid, parsed_guess, error_message = parse_guess("0", low, high)
    assert not valid
    assert parsed_guess is None
    assert error_message == "Guess must be between 1 and 100"

def test_parse_guess_out_of_bounds_high():
    # Test a guess above the upper bound
    low, high = 1, 100
    valid, parsed_guess, error_message = parse_guess("101", low, high)
    assert not valid
    assert parsed_guess is None
    assert error_message == "Guess must be between 1 and 100"

def test_parse_guess_invalid_input():
    # Test invalid input (non-numeric)
    low, high = 1, 100
    valid, parsed_guess, error_message = parse_guess("abc", low, high)
    assert not valid
    assert parsed_guess is None
    assert error_message == "That is not a number"

def test_parse_guess_empty_input():
    # Test empty input
    low, high = 1, 100
    valid, parsed_guess, error_message = parse_guess("", low, high)
    assert not valid
    assert parsed_guess is None
    assert error_message == "Enter a guess"

def test_parse_guess_edge_cases():
    # Test edge cases at the bounds
    low, high = 1, 100
    valid_low, parsed_guess_low, _ = parse_guess("1", low, high)
    valid_high, parsed_guess_high, _ = parse_guess("100", low, high)
    assert valid_low
    assert parsed_guess_low == 1
    assert valid_high
    assert parsed_guess_high == 100
