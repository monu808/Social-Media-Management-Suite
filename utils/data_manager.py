#!/usr/bin/env python3
"""
Data Manager Utility
Handles data persistence and management for the Social Media MCP Server.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

class DataManager:
    """Manages data persistence for the social media server."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.ensure_data_directory()
    
    def ensure_data_directory(self):
        """Ensure the data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)
    
    def load_json(self, filename: str) -> List[Dict[str, Any]]:
        """Load data from JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
    
    def save_json(self, filename: str, data: List[Dict[str, Any]]) -> bool:
        """Save data to JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving {filename}: {e}")
            return False
    
    def add_record(self, filename: str, record: Dict[str, Any]) -> bool:
        """Add a record to a JSON file."""
        data = self.load_json(filename)
        record['created_at'] = datetime.now().isoformat()
        data.append(record)
        return self.save_json(filename, data)
    
    def update_record(self, filename: str, record_id: str, updates: Dict[str, Any]) -> bool:
        """Update a record in a JSON file."""
        data = self.load_json(filename)
        for record in data:
            if record.get('id') == record_id:
                record.update(updates)
                record['updated_at'] = datetime.now().isoformat()
                return self.save_json(filename, data)
        return False
    
    def delete_record(self, filename: str, record_id: str) -> bool:
        """Delete a record from a JSON file."""
        data = self.load_json(filename)
        original_length = len(data)
        data = [record for record in data if record.get('id') != record_id]
        if len(data) < original_length:
            return self.save_json(filename, data)
        return False
    
    def find_records(self, filename: str, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Find records matching the given filters."""
        data = self.load_json(filename)
        results = []
        
        for record in data:
            match = True
            for key, value in filters.items():
                if record.get(key) != value:
                    match = False
                    break
            if match:
                results.append(record)
        
        return results

# Global instance
data_manager = DataManager()
