from ._anvil_designer import questionnaireTemplate
from anvil import *
import anvil.server

class questionnaire(questionnaireTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.experimentType = 'not specified'

    # Any code you write here will run before the form opens.

  def cryoprotectant_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass

  def cryoprotectantCheckBox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    if self.cryoprotectantCheckBox.checked:
      self.cryoprotectant.enabled = True
    elif not self.cryoprotectantCheckBox.checked:
      self.cryoprotectant.text = ""
      self.cryoprotectant.enabled = False
    pass

  def localMountCheckBox_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
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
    """This method is called when this radio button is selected"""
    if self.ligandRadio.selected:
      self.ligandCheckBox.checked = True
    pass

  def reset_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.collectnsend()
    anvil.server.call("recieveData", self.data)
    pass

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
      'pathologies': [self.tNCSCheck.checked, self.twinnedCheck.checked, self.LTDCheck.checked, self.anisoCheck.checked, self.multilatticeCheck.checked],
      
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

