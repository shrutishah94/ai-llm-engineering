from app.orchestration.pipeline import content_format


def main() -> None:
    demo_url = "https://example.com"
    result = content_format(demo_url)
    print("URL:\n", result["url"])
    print("\nSUMMARY:\n", result["summary"])
    print("\nEXTRACTION:\n", result["entities"])


if __name__ == "__main__":
    main()
