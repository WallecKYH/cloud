import datetime

from dotenv import load_dotenv

from app.dynamodb_access import get_item_by_id, get_item_by_attribute, get_item_by_attribute_gt


def main():


    load_dotenv()
    # item = get_item_by_id('a04f186c-94e5-11ec-ad0c-813ad375745b')
    items = get_item_by_attribute("sensor", "Temp Sensor 1")
    items = get_item_by_attribute_gt("temp", 19)
    # Convert datetime from string to datetime object
    for item in items:
        item['datetime'] = datetime.datetime.strptime(item['datetime'], "%Y-%m-%d %H:%M:%S")

    items.sort(key=lambda item: item['datetime'])
    print("First:", items[0])
    print("Last:", items[-1])
    temps = []
    for item in items:
        temps.append(item['temp'])

    temps = sorted([item['temp'] for item in items], reverse=True)

    filtered = [{'sensor': item['sensor'], 'temp': item['temp']} for item in items]
    print()


if __name__ == '__main__':
    main()