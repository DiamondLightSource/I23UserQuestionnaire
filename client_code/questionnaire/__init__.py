from ._anvil_designer import questionnaireTemplate
from anvil import *
import anvil.server
import Yosoku

class questionnaire(questionnaireTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.experimentType = 'not specified'
    self.selected_file = None

  
  def cryoprotectant_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass

  def cryoprotectantCheckBox_change(self, **event_args):
    if self.cryoprotectantCheckBox.checked:
      self.cryoprotectant.enabled = True
    elif not self.cryoprotectantCheckBox.checked:
      self.cryoprotectant.text = ""
      self.cryoprotectant.enabled = False
    pass

  def localMountCheckBox_change(self, **event_args):
    if self.localMountCheckBox.checked:
      self.mountsSize.text = ""
      self.mountsSize.enabled = False
      self.handingToolsCheckBox.checked = False
      self.handingToolsCheckBox.enabled = False
      self.address.text = ""
      self.address.enabled = False
      self.EORI.text = ""
      self.EORI.enabled = False
    elif not self.localMountCheckBox.checked:
      self.mountsSize.enabled = True
      self.handingToolsCheckBox.enabled = True
      self.address.enabled = True
      self.EORI.enabled = True
    pass

  def ligandRadio_clicked(self, **event_args):
    if self.ligandRadio.selected:
      self.ligandCheckBox.checked = True
    pass

  def reset_click(self, **event_args):
    self.name.text = ''
    self.email.text = ''
    self.group.text = ''
    self.BAG.text = ''
    self.protein.text = ''
    self.sequence.text = ''
    self.crystallisationConditions.text = ''
    self.cryoprotectantCheckBox.checked = False
    self.cryoprotectant.text = ''
    self.crystalSize.text = ''
    self.spaceGroup.selected_value = 'P1'
    self.unitCell.text = ''
    self.molPerASU.text = ''
    self.typicalRes.text = ''
    self.highRes.text = ''
    self.isomorphousCheckBox.checked = False
    self.ligandCheckBox.checked = False
    self.anomScatterer.text = ''
    self.tNCSCheck.checked = False
    self.twinnedCheck.checked = False
    self.LTDCheck.checked = False
    self.anisoCheck.checked = False
    self.multilatticeCheck.checked = False
    self.localMountCheckBox.checked = False
    self.mountsSize.text = ''
    self.handingToolsCheckBox.checked = False
    self.address.text = ''
    self.EORI.text = ''
    pass

  def submit_click(self, **event_args):
    anvil.server.call("cleanUp")
    if self.name.text == None
    self.pathologies()
    self.collectnsend()
    if self.selected_file:
      anvil.server.call('uploadPDB', self.selected_file)
    anvil.server.call("recieveData", self.data)
    pass

  def pathologies(self):
    self.pathologyString = ""
    if self.tNCSCheck.checked:
      self.pathologyString += "tNCS "
    if self.twinnedCheck.checked:
      self.pathologyString += "twinned "
    if self.LTDCheck.checked:
      self.pathologyString += "LTD "
    if self.anisoCheck.checked:
      self.pathologyString += "anisotropy "
    if self.multilatticeCheck.checked:
      self.pathologyString += "multi-lattice"
    
  def collectnsend(self):
    self.data = {
      'name': self.name.text,
      'email': self.email.text,
      'group': self.group.text,
      'BAG': self.BAG.text,
      'I23 contact': self.I23LC.selected_value,
      'experiment type': self.experimentType,
      'protein name': self.protein.text,
      'sequence': self.sequence.text,
      'conditions': self.crystallisationConditions.text,
      'LCP': self.lcpCheckBox.checked,
      'cryo needed': self.cryoprotectantCheckBox.checked,
      'cryoprotectant': self.cryoprotectant.text,
      'morphology': self.morphology.selected_value,
      'size': self.crystalSize.text,
      'space group': self.spaceGroup.selected_value,
      'unit cell': self.unitCell.text,
      'molecules per ASU': self.molPerASU.text,
      'typical resolution': self.typicalRes.text,
      'high resolution': self.highRes.text,
      'isomorphous': self.isomorphousCheckBox.checked,
      'ligand': self.ligandCheckBox.checked,
      'scatterers': self.anomScatterer.text,
      'pathologies': self.pathologyString,
      'pdb code': self.PDBcode.text,
      'local mounting': self.localMountCheckBox.checked,
      'mounts': self.mountsSize.text,
      'tools': self.handingToolsCheckBox.checked,
      'contact': self.address.text,
      'EORI': self.EORI.text,
    }

  def phasingRadio_clicked(self, **event_args):
    self.experimentType = 'phasing'
    pass

  def ionRadio_clicked(self, **event_args):
    self.experimentType = 'ion identification'
    pass

  def otherRadio_clicked(self, **event_args):
    self.experimentType = 'other'
    pass

  def PDBfile_change(self, file, **event_args):
    if file:
        valid_extensions = ['.pdb', '.cif']
        file_name = file.name
        if not any(file_name.endswith(ext) for ext in valid_extensions):
            alert("Invalid file type. Please upload a .pdb or .cif file.")
            self.selected_file = None
            return

        max_size_mb = 5
        file_size_in_bytes = len(file.get_bytes())
        if file_size_in_bytes > max_size_mb * 1024 * 1024:
            alert("File size exceeds the limit of 5 MB. Please upload a smaller file or contact the I23 team.")
            self.selected_file = None
            return

        self.selected_file = file
        alert("File selected: " + file.name)
    pass

