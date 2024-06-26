def detect_threat(content):
    threats = {
        'SQL Injection': ['1=1', 'OR', 'INSERT', 'SELECT', 'WHERE', 'union'],
        'Cross Site Scripting': ['alert', 'script', 'ALERT', 'SCRIPT'],
        'Command Injection': ['ECHO', 'DIR', 'LS', 'CP', 'CAT', 'TYPE', 'type', 'cat', 'cp', 'ls', 'dir', 'echo', 'ID', 'id'],
        'File Inclusion': ['../', '/etc/passwd', '/'],
        'Nikto': ['nikto']
    }
    
    for threat_type, keywords in threats.items():
        for keyword in keywords:
            if keyword in content:
                print(f'{threat_type} ATTACK DETECTED\n{keyword} found')
                return
    print('No threat Detected')

def main():
    print('Enter the name of the file:')
    file_name = input("Name: ")

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            detect_threat(content)
    except FileNotFoundError:
        print(f'The file {file_name} does not exist.')

if __name__ == "__main__":
    main()
