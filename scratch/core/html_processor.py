import os
import re
import logging

# Configure logging for the refactored tools
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class HTMLProcessor:
    """
    A unified engine for processing HTML files in the Hetch codebase.
    Ensures safe, atomic replacements and consistent file handling.
    """
    
    def __init__(self, base_dir=None):
        self.base_dir = base_dir or os.getcwd()
        self.processed_count = 0

    def get_html_files(self, filter_list=None):
        """Returns a list of HTML files to process."""
        if filter_list:
            return [f for f in filter_list if os.path.exists(os.path.join(self.base_dir, f))]
        return [f for f in os.listdir(self.base_dir) if f.endswith('.html')]

    def read_file(self, filename):
        """Standardized file reading with encoding fallback."""
        filepath = os.path.join(self.base_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='latin-1') as f:
                return f.read()

    def write_file(self, filename, content):
        """Standardized file writing."""
        filepath = os.path.join(self.base_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def apply_replacement(self, content, pattern, replacement, count=0):
        """Applies a regex replacement or string replacement."""
        if isinstance(pattern, re.Pattern):
            return pattern.sub(replacement, content, count=count)
        return content.replace(pattern, replacement, count or 1)

    def process_batch(self, tasks, target_files=None):
        """
        Executes a sequence of replacement tasks on a set of files.
        Each task is a dict: {'pattern': ..., 'replacement': ..., 'name': ...}
        """
        files = self.get_html_files(target_files)
        self.processed_count = 0

        for filename in files:
            content = self.read_file(filename)
            original_content = content
            
            for task in tasks:
                content = self.apply_replacement(content, task['pattern'], task['replacement'])
            
            if content != original_content:
                self.write_file(filename, content)
                logger.info(f"Updated: {filename}")
                self.processed_count += 1
            else:
                logger.debug(f"No changes for: {filename}")

        logger.info(f"Batch complete. Updated {self.processed_count} files.")
        return self.processed_count

# --- ORIGINAL CODE MARKER ---
# This engine provides the structure used by the refactored scripts.
