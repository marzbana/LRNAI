from flask import Flask, render_template, request
from vector import Vector
from doc import Doc 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        contract_sections = [
            {
                'name': 'Customer Name',
                'input_name': 'customer_name_input'
            },
            {
                'name': 'Project Scope',
                'input_name': 'project_scope_input'
            },
            {
                'name': 'Detailed Description of All Deliverables',
                'input_name': 'deliverables_input'
            },
            {
                'name': 'Detailed Timelines for Each Deliverable',
                'input_name': 'timelines_input'
            },
            {
                'name': 'Payment Terms and Schedule',
                'input_name': 'payment_terms_input'
            },
            {
                'name': 'Assumptions and Dependencies',
                'input_name': 'assumptions_input'
            },
            {
                'name': 'Risks and Mitigation Strategies',
                'input_name': 'risks_input'
            },
            {
                'name': 'Any Specific Legal or Regulatory Considerations for this Type of Work',
                'input_name': 'legal_considerations_input'
            },
            {
                'name': 'Service Level Agreement (SLA)',
                'input_name': 'sla_input'
            }
        ]

        contract_details = {}
        for section in contract_sections:
            contract_details[section['name']] = request.form[section['input_name']]

        vector = Vector()
        vector.init()
        prompt = """
Please provide a contract with the same level of detail and structure from the ies contracts you were trained on. The contract should be formatted nicely and be professional. The contract should have sections: Services, Definitions, Contractural Responsibilities, Compensation and Payment, Property Rights, Confidential Information, Representations and Warranties, Indemnifications, Non-Interference with Business, Terms and Termination, General Provisions, and a Signing section similar to the contracts you were trained on. The Company is IES and the customer name is below along with specific details that describe what was written above. The contract should accurately depict everything that is entered below and that is the most important. What is above and the contracts you were trained on are just a framework.

"""

        contract_text = "".join([f"{section['name']}: {contract_details[section['name']]}" for section in contract_sections])
        vector.setQuery(prompt + "" + contract_text)
        vector.setResponse()
        response = str(vector.getResponse())

        doc = Doc()
        filename = str(request.form['file_name_input'] + ".docx")
        doc.create_docx(response, filename)

        return render_template('result.html', response=response, filename=filename)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
