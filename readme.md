# Password Complexity Curator

Using a list of passwords (e.g. [CrackStation](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm)) and a given password complexity format, we can filter out the passwords from the list that do not satisfy a given set of password complexity requirements.

## Setting the Password Complexity Requirements
Use the following schema to specify a complexity requirement statement.
Place the JSON inside a file located at `password_requirements.json`.

  **JSON Fields:**
  
  | Field | Type | Description | Example |
  |-----|-----|-----|-------|
  | **minLength** | Number | Specifies the minimum length of the password. Must be a positive integer. | `"minLength": 8` |
  | **requirements** | Object | Contains criteria that represent individual requirements for the password. | `"requirements": {...}` |
  | __requirements.lowercase__ | Boolean | If set to `true`, requires the password to contain at least one lowercase letter. | `"lowercase": true` |
  | __requirements.uppercase__ | Boolean | If set to `true`, requires the password to contain at least one uppercase letter. | `"uppercase": true` |
  | __requirements.numeric__ | Boolean | If set to `true`, requires the password to contain at least one numeric digit. | `"numeric": true` |
  | __requirements.specialChar__| Boolean | If set to `true`, requires the password to contain at least one special character (non-alphanumeric). | `"specialChar": true` |
  | **minReqCount** | Number | Specifies the minimum number of `true` requirements from the `requirements` object that a password must meet. Must be a positive integer less than or equal to the count of criteria in `requirements`. | `"minReqCount": 3` |
  
  **Usage Guide:**
  
  To set the password conditions, edit the values according to your preference. Ensure there are at least as many `true` values in `requirements` as the value of `minReqCount`, otherwise, it would be impossible for a password to fulfill the requirements.
  
  For instance, setting `minReqCount` to `3` would require any three conditions set to `true` in the `requirements` object to be met, allowing for some flexibility in password creation. This can be adjusted according to your security requirements.
  
  Remember that this schema only acts as a guide to your program. You need to interpret and implement it in your program correctly to enforce these password requirements.

For example, to only include passwords which are:
 - over 16 characters
 - contain three of the four below requirements:
    - contain a number
    - contain a lowercase letter
    - contain an uppercase letter
    - contain a special character

We can use the following JSON:
```json
{
  "minLength": 16,
  "requirements": {
    "lowercase": true,
    "uppercase": true,
    "numeric": true,
    "specialChar": true
  },
  "minReqCount": 3
}
```

## Output Format

The output of this tool will be a plaintext list of passwords, with each line containing one password only.
