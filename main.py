import secrets
import string


def generate_password(length=16, use_upper=True, use_lower=True,
                      use_digits=True, use_symbols=True):
    """Generate a cryptographically strong random password."""
    groups = []

    if use_upper:
        groups.append(string.ascii_uppercase)
    if use_lower:
        groups.append(string.ascii_lowercase)
    if use_digits:
        groups.append(string.digits)
    if use_symbols:
        groups.append("!@#$%^&*()-_=+[]{}?")

    if not groups:
        raise ValueError("Select at least one character type.")
    if length < len(groups):
        raise ValueError(
            f"Length must be at least {len(groups)} for the selected options."
        )

    # Ensure at least one character from every selected group.
    password_chars = [secrets.choice(group) for group in groups]
    all_chars = "".join(groups)

    # Fill the remaining length and securely shuffle the result.
    password_chars.extend(
        secrets.choice(all_chars) for _ in range(length - len(password_chars))
    )
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def ask_yes_no(prompt, default=True):
    suffix = " [Y/n]: " if default else " [y/N]: "
    answer = input(prompt + suffix).strip().lower()
    if not answer:
        return default
    return answer in ("y", "yes")


def main():
    print("=" * 48)
    print("       PASSWORD GENERATOR")
    print("=" * 48)

    try:
        length_text = input("Enter password length (8-64, default 16): ").strip()
        length = int(length_text) if length_text else 16

        if not 8 <= length <= 64:
            print("Please choose a length between 8 and 64.")
            return

        upper = ask_yes_no("Include uppercase letters?")
        lower = ask_yes_no("Include lowercase letters?")
        digits = ask_yes_no("Include numbers?")
        symbols = ask_yes_no("Include special characters?")

        password = generate_password(length, upper, lower, digits, symbols)

        print("\nYour generated password:")
        print(password)
        print("\nStore it safely. Do not share it with anyone.")

    except ValueError as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
