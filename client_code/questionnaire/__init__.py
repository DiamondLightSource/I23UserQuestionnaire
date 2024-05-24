from ._anvil_designer import questionnaireTemplate
from anvil import *
import anvil.server
import pickle

class questionnaire(questionnaireTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

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
    
    pass

  def collectnpickle(self):
    data = {
      'address': self.address.text,
      'anomalous scatterer': self.anomScatterer.text,
    }