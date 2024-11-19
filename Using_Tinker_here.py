import tkinter as tk


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$',
           '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']


def cipher_gang(start_text, shift1, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift1 *= -1
    for char in start_text:
        if char in letters:
            position = letters.index(char)
            new_position = (position + shift1) % 26
            end_text += letters[new_position]
        else:
            end_text += char  # Leave non-alphabetic characters unchanged
    return end_text


# Handling the encoding action in the GUI
def on_encode():
    message = message_entry.get()  # Get message from the input field
    key = int(key_entry.get())  # Get the shift key from the input field
    encrypted_message = cipher_gang(message, key, "encode")  # Encrypt the message
    result_label.config(text=f"Encrypted: {encrypted_message}")  # Display the encrypted message


# Handling the decoding action in the GUI
def on_decode():
    encrypted_message = message_entry.get()  # Get encrypted message from the input field
    key = int(key_entry.get())  # Get the shift key from the input field
    decrypted_message = cipher_gang(encrypted_message, key, "decode")  # Decrypt the message
    result_label.config(text=f"Decrypted: {decrypted_message}")  # Display the decrypted message


# Set up the GUI window
root = tk.Tk()
root.title("Simple Messaging App with Encryption")

# Create UI elements
message_label = tk.Label(root, text="Enter your message:")
message_label.pack()

message_entry = tk.Entry(root, width=60)  # Input field for the message
message_entry.pack()

key_label = tk.Label(root, text="Enter your shift key:")
key_label.pack()

key_entry = tk.Entry(root, width=60)  # Input field for the shift key
key_entry.pack()

encode_button = tk.Button(root, text="Encode", command=on_encode)  # Button for encoding
encode_button.pack()

decode_button = tk.Button(root, text="Decode", command=on_decode)  # Button for decoding
decode_button.pack()

result_label = tk.Label(root, text="")  # Label to display the result
result_label.pack()

# Run the app
root.mainloop()
