import platform
import psutil
import tiktoken
import google.generativeai as genai

# Read API keys from keys.txt
def read_keys(filepath='keys.txt'):
    keys = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    keys[k.strip()] = v.strip()
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Please create it and add your keys.")
    return keys

def get_connection_type():
    interfaces = psutil.net_if_stats()
    for iface_name, iface in interfaces.items():
        if iface.isup:
            if "wi-fi" in iface_name.lower():
                return "WiFi"
            if "ethernet" in iface_name.lower():
                return "Ethernet"
            if "wireless" in iface_name.lower():
                return "Wireless (possibly WiFi)"
    return "Unknown"

def get_device_type():
    system = platform.system()
    if system == 'Windows':
        return "Windows PC"
    elif system == 'Darwin':
        return "Mac"
    elif system == 'Linux':
        uname = platform.uname()
        if 'android' in uname.release.lower():
            return "Android"
        else:
            return f"Linux ({uname.machine})"
    return f"Other: {system}"

def print_device_info():
    device = get_device_type()
    connection = get_connection_type()
    print(f"\nDEVICE: {device}")
    print(f"CONNECTION: {connection}\n")

def count_tokens(text, model_name="gemini-1.5-pro-latest"):
    try:
        enc = tiktoken.encoding_for_model("gpt-4o")
        return len(enc.encode(text))
    except Exception:
        return 0

def select_response_length():
    print("\nChoose response length:")
    print("1) Very Short (≤10 words)")
    print("2) Short (≤50 words)")
    print("3) Medium (≤150 words)")
    print("4) Long (no limit)")
    choice = input("Select option (1/2/3/4): ").strip()
    if choice == '1':
        return "very_short"
    elif choice == '2':
        return "short"
    elif choice == '3':
        return "medium"
    else:
        return "long"

def chat_with_gemini(message, length_choice):
    model_name = "gemini-1.5-pro-latest"
    if length_choice == "very_short":
        message += "\n\nPlease answer in 10 words or fewer."
    elif length_choice == "short":
        message += "\n\nPlease answer in about 50 words or fewer."
    elif length_choice == "medium":
        message += "\n\nPlease answer 150 words or fewer, please."
    try:
        response = genai.chat(messages=[message])
        reply = response.last
        if length_choice == "very_short":
            reply = ' '.join(reply.split()[:10])
        reply_tokens = count_tokens(reply)
        return reply, reply_tokens
    except Exception as e:
        return f"Error: {str(e)}", 0

def main():
    keys = read_keys()
    if "GOOGLE_AI_STUDIO_API_KEY" not in keys:
        print("Error: GOOGLE_AI_STUDIO_API_KEY not found in keys.txt.")
        return
    genai.configure(api_key=keys["GOOGLE_AI_STUDIO_API_KEY"])

    print("\n--- Google AI Studio Gemini Controller ---")
    print_device_info()
    print("Using model: gemini-1.5-pro-latest")

    while True:
        print("\n--- New Query ---")
        query = input("Enter your message (or type 'quit' to exit): ").strip()
        if query.lower() in ['quit', 'exit', 'q']:
            break

        length_choice = select_response_length()
        reply, reply_tokens = chat_with_gemini(query, length_choice)

        print("\nREPLY:")
        print("-" * 40)
        print(reply)
        print("-" * 40)
        print(f"Tokens (estim.): {reply_tokens if reply_tokens is not None else 'N/A'}")
        if length_choice == "very_short":
            word_count = len(reply.split())
            print(f"Actual word count: {word_count} (requested ≤10)")

if __name__ == "__main__":
    main()
