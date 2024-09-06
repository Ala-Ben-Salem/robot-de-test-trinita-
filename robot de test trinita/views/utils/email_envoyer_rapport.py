import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(subject, body, to_email, attachment_folder):
    from_email = 'bensalem.ala22@gmail.com'  # Remplacez par votre adresse e-mail
    from_password = 'znrj bmvm tspn ktlv'     # Remplacez par votre mot de passe ou mot de passe d'application

    # Créer le message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Ajouter le corps du message
    msg.attach(MIMEText(body, 'plain'))

    # Ajouter le fichier Word comme pièce jointe
    for file_name in os.listdir(attachment_folder):
        if file_name.endswith('.docx'):  # Vérifier si le fichier est un fichier Word
            file_path = os.path.join(attachment_folder, file_name)
            if os.path.isfile(file_path):
                part = MIMEBase('application', 'octet-stream')
                with open(file_path, 'rb') as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
                msg.attach(part)
                #break  # Sortir de la boucle après avoir trouvé et attaché le fichier Word

    # Envoyer l'e-mail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Serveur SMTP de Gmail
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(msg)
        server.quit()
        print("E-mail envoyé avec succès")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail: {e}")