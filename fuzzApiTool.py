import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

def fuzzFun(url, parameter):
    try:
        res = requests.get(url + parameter)
        # res.raise_for_status()

        if res.status_code == 404:
            # logging.info(f"Parameter {parameter} not found")
            print(f">> 404 {parameter} ")
        else:
            with open('jsonFile.txt','a')as f1:
                data = f1.write(res.json()," -> ",res.status_code,"\n")

                data = res.json()
                # logging.info(f"res for {parameter}: {data}")
                print(f">>>>>>>>>>>>Response for {parameter}: {data}")
            

    except requests.exceptions.RequestException as e:
        # logging.error(f"Error for {parameter}: {e}")
        print(f">>>>Error for: {parameter}: {e}")

def main():
    logging.info("API fuzz tool connecting to the domain...")

    domainName = "https://therubmind.com/"

    parameterFile = "apiParameter.txt"

    with open(parameterFile, "r") as f:
        try:
            for no, line in enumerate(f, start=1):
                logging.info(f"Injecting payload {no}...")
                word = line.strip()
                fuzzFun(domainName, word)
        except KeyboardInterrupt:
            print("exit")

    logging.info("DONE")

if __name__ == "__main__":
    main()
