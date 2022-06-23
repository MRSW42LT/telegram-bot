from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ('oi'):
        return ']oi, funcionando.'
    
    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:S')
        
        return str(date_time)

    return 'Erro'