import os
import shutil
from pathlib import Path
from config import FILE_CATEGORIES


class FileOrganizer:
    
    def __init__(self, source_path: str):

        #source_path: Caminho da pasta a organizar
        
        self.source_path = Path(source_path)
        self.results = {
            "moved": 0,
            "errors": 0,
            "skipped": 0,
            "details": []
        }
    
    def get_category(self, filename: str) -> str:
        file_ext = Path(filename).suffix.lower()
        
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                return category
        
        return "Outros"
    
    def organize(self) -> dict:
        # Organiza os arquivos da pasta de origem
        # Retorna um dicionário com os resultados da organização
        if not self.source_path.exists():
            self.results["errors"] += 1
            self.results["details"].append(f"Pasta não encontrada: {self.source_path}")
            return self.results
        
        try:
            # Itera sobre os arquivos da pasta
            for item in self.source_path.iterdir():
                # Ignora pastas
                if item.is_dir():
                    continue
                
                # Pula arquivos do sistema
                if item.name.startswith("."):
                    self.results["skipped"] += 1
                    continue
                
                # Determina a categoria
                category = self.get_category(item.name)
                
                # Cria a pasta de destino se não existir
                dest_folder = self.source_path / category
                dest_folder.mkdir(exist_ok=True)
                
                # Move o arquivo
                try:
                    dest_file = dest_folder / item.name
                    
                    # Se o arquivo já existe, adiciona um sufixo
                    if dest_file.exists():
                        name = item.stem
                        ext = item.suffix
                        counter = 1
                        while dest_file.exists():
                            dest_file = dest_folder / f"{name}_{counter}{ext}"
                            counter += 1
                    
                    shutil.move(str(item), str(dest_file))
                    self.results["moved"] += 1
                    self.results["details"].append(f"✓ Movido: {item.name} → {category}/")
                
                except Exception as e:
                    self.results["errors"] += 1
                    self.results["details"].append(f"✗ Erro ao mover {item.name}: {str(e)}")
        
        except Exception as e:
            self.results["errors"] += 1
            self.results["details"].append(f"Erro geral: {str(e)}")
        
        return self.results
    
    def get_folder_structure(self) -> dict:
        # Retorna a estrutura atual da pasta
        # Retorna um dicionário com informações sobre os arquivos e pastas
        structure = {
            "total_files": 0,
            "categories": {},
            "unorganized": []
        }
        
        if not self.source_path.exists():
            return structure
        
        try:
            for item in self.source_path.iterdir():
                if item.is_dir():
                    # Conta arquivos em subpastas
                    files_count = len([f for f in item.iterdir() if f.is_file()])
                    if files_count > 0:
                        structure["categories"][item.name] = files_count
                elif item.is_file() and not item.name.startswith("."):
                    structure["unorganized"].append(item.name)
                    structure["total_files"] += 1
        
        except Exception as e:
            structure["error"] = str(e)
        
        return structure
