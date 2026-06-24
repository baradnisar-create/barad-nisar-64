from urllib.parse import urlparse

def scan_url(url):
    suspicious_words = [
        "login", "verify", "secure", "update",
        "bank", "free", "bonus", "win", "gift"
    ]

    parsed = urlparse(url)

    print("\n----- URL Scan Report -----")
    print("Domain:", parsed.netloc)
    print("Protocol:", parsed.scheme)

    score = 0

    # HTTPS Check
    if parsed.scheme != "https":
        print("⚠ No HTTPS detected")
        score += 1
    else:
        print("✓ HTTPS Enabled")

    # URL Length Check
    if len(url) > 50:
        print("⚠ Long URL")
        score += 1

    # Suspicious Keywords
    for word in suspicious_words:
        if word in url.lower():
            print(f"⚠ Suspicious keyword found: {word}")
            score += 1

    # Final Result
    print("\nRisk Score:", score)

    if score >= 3:
        print("🔴 High Risk (Possible Phishing)")
    elif score >= 1:
        print("🟡 Medium Risk")
    else:
        print("🟢 Safe URL")

url = input("Enter URL: ")
scan_url(url)