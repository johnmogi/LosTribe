import pygame
import os
import json

class ResourceManager:
    def __init__(self):
        self.loaded_resources = {}
        self.resource_paths = {
            'sprites': {},
            'sounds': {},
            'music': {}
        }
        self.current_section = None
        
    def load_section(self, section_name):
        """Load resources for a specific game section"""
        if self.current_section == section_name:
            return
            
        # Unload previous section resources
        self.unload_section()
        
        # Load new section resources
        self.current_section = section_name
        section_data = self.resource_paths.get(section_name, {})
        
        for resource_type, resources in section_data.items():
            for resource_name, path in resources.items():
                self.load_resource(resource_type, resource_name, path)
                
    def unload_section(self):
        """Unload all resources from current section"""
        if self.current_section:
            for resource in self.loaded_resources.values():
                if hasattr(resource, 'unload'):
                    resource.unload()
            self.loaded_resources.clear()
            self.current_section = None
            
    def load_resource(self, resource_type, name, path):
        """Load a single resource"""
        if resource_type == 'sprites':
            resource = pygame.image.load(path).convert_alpha()
        elif resource_type == 'sounds':
            resource = pygame.mixer.Sound(path)
        elif resource_type == 'music':
            resource = path  # Store path only, load when playing
        else:
            return None
            
        self.loaded_resources[name] = resource
        return resource
        
    def get_resource(self, name):
        """Get a loaded resource by name"""
        return self.loaded_resources.get(name)
        
    def play_music(self, name):
        """Play music track by name"""
        if name in self.loaded_resources:
            path = self.loaded_resources[name]
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)  # Loop indefinitely
            
    def stop_music(self):
        """Stop currently playing music"""
        pygame.mixer.music.stop()
        
    def play_sound(self, name):
        """Play sound effect by name"""
        sound = self.get_resource(name)
        if sound:
            sound.play()
            
    def add_resource_path(self, section, resource_type, name, path):
        """Add a resource path to be loaded later"""
        if section not in self.resource_paths:
            self.resource_paths[section] = {}
        if resource_type not in self.resource_paths[section]:
            self.resource_paths[section][resource_type] = {}
        self.resource_paths[section][resource_type][name] = path
