'''Indexer class
'''
# Python modules
import os
import git
import argparse
# Source index modules
from . import pdb
from . import base


class Indexer(base.Base):
    '''Source indexer class
    '''
    def __init__(self, args):
        super(Indexer, self).__init__(args)

        if not args.build_base.endswith('\\'):
            args.build_base = args.build_base + '\\'
            
        try:
            if not self.args.hexsha or len(self.args.hexsha) != 40:
                raise ValueError
            int(self.args.hexsha, 16)
        except ValueError:
            self.repo = git.Repo(self.args.build_base)
            self.args.hexsha = self.repo.active_branch.object.hexsha

    def _index(self):
        ''' Initial indexing during build
        '''
        for bld_dir in self.args.pdbs:
            bld_dir = os.path.join(self.args.build_base, bld_dir)
            if not os.path.isdir(bld_dir):
                self.logger.error('Directory: {bld_dir} not found')
                continue    # Non-fatal error, skip invalid directory

            for dir, subdirs, files in os.walk(bld_dir):
                for fname in files:
                    if fname.endswith('.pdb'):
                        self.args.pdb = os.path.join(dir, fname)
                        self.args.output = argparse.FileType('w')(self.args.pdb[:-4] + '.ini')
                        pdb.PDB(self.args).process(self)

    def _reindex(self):
        ''' @TODO: Process .PDB files after build. This assumes that there's a
                   way to tie back the symbols to the original repo commit hash.
        '''
        pass

    def process(self):
        ''' Process each of the .PDBs
        '''
        if not self.args.pdbs:
            return pdb.PDB(self.args).process()

        if self.args.action == 1:
            self._index()
        else:
            self._reindex()


__all__ = ['Indexer']
