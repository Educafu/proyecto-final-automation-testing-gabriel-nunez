import logging
import os
from datetime import datetime

def setup_logger(name, log_file, level=logging.INFO):
    """Configura un logger con formato específico"""
    
    # Crear directorio si no existe
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

def get_logger(name):
    """Obtiene un logger configurado"""
    log_file = f"logs/{name}_{datetime.now().strftime('%Y%m%d')}.log"
    return setup_logger(name, log_file)

# Logger por defecto
logger = get_logger("test_framework")
