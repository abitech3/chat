python -m venv venv

activate(){
    . venv/sctripts/activate
    echo "install requirement to virtual environment"
    pip install -r reguirements.txt
}

activate