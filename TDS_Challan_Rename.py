import os
import pdfplumber
import re
import sys
T = True

#--- CHALLAN RENAMER START MESSAGE ---

print("=" * 65)
print("             🚀 Income Tax Challan Renamer (v1.0) 🐍")
print("                  By: CA Finalist Jaidev Duggal")
print("=" * 65)
print("💡 This tool automates the renaming of Income Tax Challan PDFs.")
print("=" * 65)
print("🔗 Connect with me for more Automation Projects:")
print("   - LinkedIn: https://www.linkedin.com/in/jaidev-duggal")
print("   - GitHub:   https://github.com/JaidevDuggal")
print("=" * 65)
print("\n[INSTRUCTION]: Please enter the Full Path of the folder containing your Challans.")
print("    Example Path: C:\\Users\\Public\\MyChallans")
print("\n[EXIT]: To close the application, simply press Enter on an empty line.\n")
print("=" * 65)

#--- END OF MESSAGE ---

while T :
    # Input from user
    folder = input("Enter folder path: ").strip()
    #entity = input("Enter entity name: ").strip()

    if folder == "" :
        T = False
        sys.exit()

    else :
        
        try :

            for file in os.listdir(folder):
                if file.lower().endswith(".pdf"):
                    file_path = os.path.join(folder, file)

                    with pdfplumber.open(file_path) as pdf:
                        text = ""
                        for page in pdf.pages:
                            text += page.extract_text() + "\n"

                    # Extract Section (like 94I, 194J, etc.)
                    section_match = re.search(r'Nature of Payment\s*[:\-]?\s*(.+)', text, re.IGNORECASE)
                    section = section_match.group(1).upper() if section_match else "UNKNOWN"

                    # Extract Challan Number (numeric sequence)
                    challan_match = re.search(r'Challan\s*No\.?\s*[:\-]?\s*(\d+)', text, re.IGNORECASE)
                    challan_no = challan_match.group(1) if challan_match else "0000"

                    # Extract Entity Name
                    name_match = re.search(r'Name\s*[:\-]?\s*(.+)', text, re.IGNORECASE)
                    entity = name_match.group(1).strip() if name_match else "UNKNOWN"

                    # New filename format
                    new_name = f"{section} CH_No. {challan_no} {entity}.pdf"
                    new_path = os.path.join(folder, new_name)

                    os.rename(file_path, new_path)
                    print(f"Renamed: {file} -> {new_name}")

            print("\nAll PDF files renamed successfully! \n")
        except : 
            print("Please Enter a Valid Path \n")
            #T = False
            #sys.exit()

