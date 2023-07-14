from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QWidget
from vector import Vector
from doc import Doc 

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter API Key")

        self.file_name_input = QLineEdit()
        self.file_name_input.setPlaceholderText("Enter File Name")

        self.customer_name_input = QLineEdit()
        self.customer_name_input.setPlaceholderText("Enter Customer Name")

        self.project_scope_input = QTextEdit()
        self.project_scope_input.setPlaceholderText("Enter Project Scope")

        self.deliverables_input = QTextEdit()
        self.deliverables_input.setPlaceholderText("Enter Detailed Description of All Deliverables")

        self.timelines_input = QTextEdit()
        self.timelines_input.setPlaceholderText("Enter Detailed Timelines for Each Deliverable")

        self.payment_terms_input = QTextEdit()
        self.payment_terms_input.setPlaceholderText("Enter Payment Terms and Schedule")

        self.assumptions_input = QTextEdit()
        self.assumptions_input.setPlaceholderText("Enter Assumptions and Dependencies")

        self.risks_input = QTextEdit()
        self.risks_input.setPlaceholderText("Enter Risks and Mitigation Strategies")

        self.legal_considerations_input = QTextEdit()
        self.legal_considerations_input.setPlaceholderText("Enter Any Specific Legal or Regulatory Considerations for this Type of Work")

        self.sla_input = QTextEdit()
        self.sla_input.setPlaceholderText("Enter Service Level Agreement (SLA)")

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.go_clicked)

        self.docx_button = QPushButton("Make .docx")
        self.docx_button.clicked.connect(self.docx_clicked)

        self.pdf_button = QPushButton("Make .pdf")
        self.pdf_button.clicked.connect(self.pdf_clicked)

        self.output_text = QTextEdit()

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.api_key_input)
        layout.addWidget(self.file_name_input)
        layout.addWidget(self.customer_name_input)
        layout.addWidget(self.project_scope_input)
        layout.addWidget(self.deliverables_input)
        layout.addWidget(self.timelines_input)
        layout.addWidget(self.payment_terms_input)
        layout.addWidget(self.assumptions_input)
        layout.addWidget(self.risks_input)
        layout.addWidget(self.legal_considerations_input)
        layout.addWidget(self.sla_input)
        layout.addWidget(self.go_button)
        layout.addWidget(self.output_text)
        layout.addWidget(self.docx_button)
        layout.addWidget(self.pdf_button)

        # Set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a vector and docx object
        self.doc = Doc()
        self.vector = Vector()
        self.vector.init()

        # Variables
        self.response = ""
        self.filename = ""
        self.prompt= """
Please provide a contract with the same level of detail and structure from the ies contracts you were trained on. The contract should be formatted nicely and be professional. The contract should have sections: Services, Definitions, Contractural Responsibilities, Compensation and Payment, Property Rights, Confidential Information, Representations and Warranties, Indemnifications, Non-Interference with Business, Terms and Termination, General Provisions, and a Signing section similar to the contracts you were trained on. The Company is IES and the customer name is below along with specific details that describe what was written above. The contract should accurately depict everything that is entered below and that is the most important. What is above and the contracts you were trained on are just a framework.  

"""

    def go_clicked(self):
        contract_details = f"""
        Customer Name: {self.customer_name_input.text()}
        Project Scope: {self.project_scope_input.toPlainText()}
        Detailed Description of All Deliverables: {self.deliverables_input.toPlainText()}
        Detailed Timelines for Each Deliverable: {self.timelines_input.toPlainText()}
        Payment Terms and Schedule: {self.payment_terms_input.toPlainText()}
        Assumptions and Dependencies: {self.assumptions_input.toPlainText()}
        Risks and Mitigation Strategies: {self.risks_input.toPlainText()}
        Any Specific Legal or Regulatory Considerations for this Type of Work: {self.legal_considerations_input.toPlainText()}
        Service Level Agreement (SLA): {self.sla_input.toPlainText()}
        """
        if(self.vector.isSet()):
            self.vector.setQuery(self.prompt + "\n" + contract_details)
            self.vector.setResponse()
            self.response = str(self.vector.getResponse())
            self.output_text.append(self.response)
        else:
            self.output_text.append("Error")

    def docx_clicked(self):
        self.filename = str(self.file_name_input.text() + ".docx")
        self.doc.create_docx(str(self.response), self.filename)


    def pdf_clicked(self):
        self.filename = str(self.file_name_input.text() + ".pdf")
        self.doc.create_pdf(str(self.response), self.filename)


if __name__ == "__main__":
    run_app()

def run_app():
    # Create a Qt application
    app = QApplication([])

    # Create and show the main window
    window = MyMainWindow()
    window.show()

    # Start the Qt event loop
    app.exec()

