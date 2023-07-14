from flask import Flask, render_template, request
from vector import Vector
from doc import Doc 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        contract_details = """
        Customer Name: {}
        Project Scope: {}
        Detailed Description of All Deliverables: {}
        Detailed Timelines for Each Deliverable: {}
        Payment Terms and Schedule: {}
        Assumptions and Dependencies: {}
        Risks and Mitigation Strategies: {}
        Any Specific Legal or Regulatory Considerations for this Type of Work: {}
        Service Level Agreement (SLA): {}
        """.format(request.form['customer_name_input'], request.form['project_scope_input'], request.form['deliverables_input'], request.form['timelines_input'], request.form['payment_terms_input'], request.form['assumptions_input'], request.form['risks_input'], request.form['legal_considerations_input'], request.form['sla_input'])

        vector = Vector()
        vector.init()
        prompt = """
Please provide a contract with the same level of detail and structure from the ies contracts you were trained on. The contract should be formatted nicely and be professional. The contract should have sections: Services, Definitions, Contractural Responsibilities, Compensation and Payment, Property Rights, Confidential Information, Representations and Warranties, Indemnifications, Non-Interference with Business, Terms and Termination, General Provisions, and a Signing section similar to the contracts you were trained on. The Company is IES and the customer name is below along with specific details that describe what was written above. The contract should accurately depict everything that is entered below and that is the most important. What is above and the contracts you were trained on are just a framework.

"""

        vector.setQuery(prompt + "
" + contract_details)
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
