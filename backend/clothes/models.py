from django.db import models

class Brand(models.Model):
    """
    브랜드 
    """
    name_kor = models.CharField()
    name_eng = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Clothes(models.Model):
    """
    옷 1개 
    신발 1개 
    
    official_product_name VARCHAR(255) NOT NULL,
    official_product_code VARCHAR(100) NOT NULL,
    brand_id INT NOT NULL,
    official_size VARCHAR(50) NOT NULL,
    internal_name VARCHAR(255),
    gender ENUM('M', 'F', 'U') NOT NULL COMMENT 'M: 남성, F: 여성, U: 유니섹스',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    status ENUM('1', '2') NOT NULL DEFAULT '1' COMMENT '1: active, 2: expired',
    UNIQUE KEY unique_product (official_product_code, brand_id, official_size),
    FOREIGN KEY (brand_id) REFERENCES brand(brand_id)    
    """
    code = "" 
    name_kor = ""
    name_eng = ""
    status = models.CharField()
    gender = models.CharField()
    brand = models.ForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    