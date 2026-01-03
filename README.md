
---
# Automated Vigenère Cipher Decoder
This project is intended to be an automated Vigenère decipherment tool designed to identify potential key length based on index of coincidence (IoC). Further implementations will include automated key-identification functionality.

- ⚠️ The code is only supports encrypted English texts   
- ⚠️ Simplistic version (for now): It detects and stops on the first instance of an IoC value between the English IOC threshold of $0.068 \pm 0.03$.    
- ⚠️ If the program does not work: Please see replies 1, 5, 16 and 19 [here](https://programmerhumor.io/debugging-memes/it-works-on-my-machine-2/).


This code is not perfect, but it is better than *my* alternative which included Python, Excel and performing calculations by hand.  


---
# Repo TODOs
- Add vigenere decoder functionality
    - Include graphs to the jupyter notebook.
- Add support for different languages
    - Develop a list of IoC values for different languages. 
    - Add language libraries: Language, alphabet, IoC value.  
- Add a simplified IoC explanation
- Add option to not specify language, identify language by IoC value. 