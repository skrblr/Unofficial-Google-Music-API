#!/usr/bin/env python

#Copyright 2012 Simon Weber.

#This file is part of gmusicapi - the Unofficial Google Music API.

#Gmusicapi is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#Gmusicapi is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with gmusicapi.  If not, see <http://www.gnu.org/licenses/>.


"""
Provides a layer of abstractions on top of Api.
"""

from api import Api

#namedtuple: mutation
# represents a change that can be made in one api call (not necessarily atomic on the server!)
# on: song, playlist
# id: for ud
# how: create, update, delete
# data: (func that updates, (args, kwargs)) to be passed

class Library:
    """Represents and allows manipulation of all data in a user's account.

    A Library is logged in to an account when initialized."""

    
    
    def __init__(self, email, password, batch_changes=False):
        """Initialize a Library with data from an account.
        Return None on login failure.
        
        :param email: 
        :param password:
        :param batch_changes: if False, push changes as they are made. If True, changes wait to be manually pushed.
        """

        self.api = Api()
        self.api.login(email, password)
        if not self.api.is_authenticated():
            #How do we fail out of init and return None on failure?
            pass

        
        self.batch_changes = batch_changes

        #The state of data on the server.
        #This only gets changed when we receive data from the server.
        self._s_songs = {}
        self._s_playlists = {}

        
        #populate songs/playlists
        #
        #

        #Our local copy of the data.
        #Unused when not batching changes.
        self._l_songs = {}
        self._l_playlists = {}

        if self.batch_changes:
            #copy in server data to local
            #ensure no cross refs
            pass
        
        #Collections of mutations not yet pushed to the server.
        #Again, unused when not batching changes.
        self._new_songs = set() #all ids are local
        self._changed_songs = set() #ids can be local/server
        self._deleted_songs = set() #ids can be local/server

        self._new_playlists = set()
        self._changed_playlists = set()
        self._deleted_playlists = set()

        #define our local id generator
        #can this be done inline (like lamdba)? or do we need to declare it
        
        
    
    def search_songs(self, locally=True, current=True):#local vs server (api) search, local current vs local server
        #use gmtools here - should probably clean gmtools
        #if not locally wrap api.search()
        pass



    ##Synchronizing changes:

    #Update our copy of the server's data.
    #Optionally reset our data to match it.
    def pull(self, reset_local=True):
        pass

    #Pushes a single change and verifies it.
    #Updates our copy of the server data on success.
    #Updates local id on creations.
    def push(self, mutation):
        pass

    #Pushes all outstanding mutations.
    #If this succeeds, local data == server data.
    #if a change fails, halt immediately, pull server data, keep our changes, and reraise.
    def push_all(self):
        pass
    
    ##Making changes to data:

    #Creation is only action done straight through Library (ie, not through a Song or Playlist).
    #So, these are public.
    def upload_song(self, filename):
        pass
    def create_playlist(self, name):
        pass

    #Update and delete are done through Songs and Playlists, so these are hidden.
    def _change_song_metadata(self, sid, key, new_val):
        pass
    def _delete_song(self, sid):
        pass


    def _change_playlist(self, pid, desired_playlist):
        pass
    def _delete_playlist(self, pid):
        pass

class Song:
    #has an id - read only
    #uses id for hashing/comparison
    #has a library

    #can delete itself from the Library
    
    #hooks a[] for metadata
    # check Expectations:
    #   valid? write through to Library dict
    #   not valid? 
    #     not existant: keyError
    #     violates expectations: ?Error

    #can get stream/download urls
    
    pass

class Playlist:
    #has immutable id
    #uses id for comp/hashing

    #has mutable name

    #has an immutable type - one of "auto", "instant", "user"
    # this determines if the playlist is mutable

    #has a library
    pass
