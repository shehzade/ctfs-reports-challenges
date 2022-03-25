/* 
 * Notes ---
 * 
 * Your encryption key must include ALL the following characters (to account for upper/lowercase):
 * {XZNLWEBGJHQDYVTKFUOMPCIASRxznlwebgjhqdyvtkfuompciasr}
 * You may randomize them as you wish at https://www.browserling.com/tools/random-letters
 * 
 * */

#include<iostream>
#include<string>

using namespace std;

string encryptMessage(string messageToEncrypt, string keyToEncryptWith);
string decryptMessage(string messageToDecrypt, string keyToDecryptWith);
void displayMenu();
void getUserSelection(char &userSelection);
void replaceSpecialChars(string &messageToEncrypt);
void getMessageToEncrypt(string &variableToStoreItIn);
void getMessageToDecrypt(string &variableToStoreItIn);
void getCipherKey(string &variableToStoreItIn);
void displayResult(int encryptedOrDecrypted, string messageToEncryptOrDecrypt, string keyToEncryptOrDecryptWith);


const string alphabetArray = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 01234567890";
const int ENCRYPTED_RESULT = 1;
const int DECRYPTED_RESULT = 0;


int main()
{
	string messageToEncrypt = "";
	string keyToEncryptWith = "";
	
	string messageToDecrypt = "";
	string keyToDecryptWith = "";
	
	char userSelection = '0';
	bool exitFlag = false;
	
	while(exitFlag == false)
	{
		displayMenu();
		getUserSelection(userSelection);
		
		switch(userSelection)
		{
			case 'e':
			case 'E':				
				getMessageToEncrypt(messageToEncrypt);
				replaceSpecialChars(messageToEncrypt);
				getCipherKey(keyToEncryptWith);
				displayResult(ENCRYPTED_RESULT, messageToEncrypt, keyToEncryptWith);
				break;
			case 'd':
			case 'D':
				getMessageToDecrypt(messageToDecrypt);
				getCipherKey(keyToDecryptWith);
				displayResult(DECRYPTED_RESULT, messageToDecrypt, keyToDecryptWith);
				break;
			case 'q':
			case 'Q':
				exitFlag = true;
				cout << endl;
				break;
			default:
				cout << endl << "Please enter a valid menu option!" << endl << endl;
				
		}
		
		}
	
	
	return 0;
}

string encryptMessage(string messageToEncrypt, string keyToEncryptWith)
{
	keyToEncryptWith += "*01234567890";
	string encryptedMessage = "";
	
	for(size_t i = 0; i < messageToEncrypt.length(); i++)
	{
		for(size_t g = 0; g < alphabetArray.length(); g++)
		{
			if(messageToEncrypt.at(i) == alphabetArray.at(g))
			{
				encryptedMessage += keyToEncryptWith.at(g);
			}
		}
	}
	
	return encryptedMessage;
		
}

string decryptMessage(string messageToDecrypt, string keyToDecryptWith)
{
	keyToDecryptWith += "*01234567890";
	string decryptedMessage = "";
	
	for(size_t i = 0; i < messageToDecrypt.length(); i++)
	{
		for(size_t g = 0; g < keyToDecryptWith.length(); g++)
		{
			if(messageToDecrypt.at(i) == keyToDecryptWith.at(g))
			{
				decryptedMessage += alphabetArray.at(g);
			}
		}
	}
	
	return decryptedMessage;
		
}

void displayMenu()
{
	cout << "==========| Welcome to the Substitution Cipher Encryptor/Decryptor |============" << endl << endl;
		
		cout << "E - Encrypt a message" << endl;
		cout << "D - Decrypt a message" << endl;
		cout << "Q - Quit the program" << endl;
}

void getUserSelection(char &userSelection)
{
	cout << endl << "Please select an option from the menu above: ";
	cin >> userSelection;
}

void getMessageToEncrypt(string &variableToStoreItIn)
{
	cout << endl << "Please enter the message you would like to encrypt: ";
	cin.ignore();
	getline(cin, variableToStoreItIn);
}

void getMessageToDecrypt(string &variableToStoreItIn)
{
	cout << endl << "Please enter the message you would like to decrypt: ";
	cin.ignore();
	getline(cin, variableToStoreItIn);
}

void getCipherKey(string &variableToStoreItIn)
{
	cout << endl << "Please enter your 52-digit key: " << endl;
	cin >> variableToStoreItIn;
}

void replaceSpecialChars(string &messageToEncrypt)
{
	bool specialCharFlag = false;
	for(size_t i = 0; i < messageToEncrypt.length(); i++)
	{
		if
		((messageToEncrypt[i] >= 65 && messageToEncrypt[i] <= 90) || 
		(messageToEncrypt[i] >= 97 && messageToEncrypt[i] <= 122) || 
		(messageToEncrypt[i] == 32) ||
		(messageToEncrypt[i] >= 48 && messageToEncrypt[i] <= 57))
		{
			continue;
		}
		else
		{
			specialCharFlag = true;
			messageToEncrypt[i] = 32;
		}
	}
	
	if(specialCharFlag)
		cout << endl << "[WARNING] All special characters in your message were replaced with spaces!" << endl;
}

void displayResult(int encryptedOrDecrypted, string messageToEncryptOrDecrypt, string keyToEncryptOrDecryptWith)
{
	if(encryptedOrDecrypted == ENCRYPTED_RESULT)
		cout << endl << "Your encrypted message is: " << encryptMessage(messageToEncryptOrDecrypt , keyToEncryptOrDecryptWith) << endl << endl;
	else
		cout << endl << "Your decrypted message is: " << decryptMessage(messageToEncryptOrDecrypt, keyToEncryptOrDecryptWith) << endl << endl;
}