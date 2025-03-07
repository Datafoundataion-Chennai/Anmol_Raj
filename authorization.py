{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f6f69816-2951-40a4-b306-00ec1cce6dbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# authorization.py\n",
    "import re\n",
    "import json\n",
    "import logging\n",
    "\n",
    "# Set up logging (console output only)\n",
    "logging.basicConfig(level=logging.INFO, format=\"%(asctime)s - %(levelname)s - %(message)s\")\n",
    "\n",
    "class LaunchAuthorizationSystem:\n",
    "    \"\"\"Handles nuclear launch authorization validation.\"\"\"\n",
    "    \n",
    "    AUTH_PATTERN = r\"^AUTH-[A-Z0-9]{3,6}-\\d{4}-SECURE$\"  # Regex for security code validation\n",
    "\n",
    "    @staticmethod\n",
    "    def validate_code(code):\n",
    "        \"\"\"Validates the launch authorization code.\"\"\"\n",
    "        if re.match(LaunchAuthorizationSystem.AUTH_PATTERN, code):\n",
    "            logging.info(\"Authorization Code Validated Successfully!\")\n",
    "            return True\n",
    "        else:\n",
    "            logging.warning(\"Invalid Authorization Code!\")\n",
    "            return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "348919d3-4901-4b1e-b7f9-49c091e526b6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
