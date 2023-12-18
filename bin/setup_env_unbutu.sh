python3 -m venv venv

activate(){
    . venv/bin/activate
    echo "install requirement to virtual environment"
    pip install -r reguirements.txt
}

activate