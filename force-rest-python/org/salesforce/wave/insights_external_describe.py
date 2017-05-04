import pprint
import json

from org.salesforce.wave.insights_external_data import InsightsExternalData


if __name__ == "__main__":
    insights_external_data = InsightsExternalData()
    data = insights_external_data.describe()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.loads(data))
