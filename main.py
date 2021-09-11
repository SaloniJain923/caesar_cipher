from caesar_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  new_text = ""
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      new_text += alphabet[new_position]
    else :
      new_text += char
  print(f"The {direction}d Message : {new_text}")

end = True
while end :
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
  text= input("Type your message: \n")
  shift = int(input("Type the shift number: \n"))
  shift =shift % 26
  caesar(text = text,shift=shift,direction=direction)

  restart= input("Type 'yes' if you want to go again. Otherwise type 'no' :\n")
  if restart == "no":
    end = False
    print("GoodBYE")