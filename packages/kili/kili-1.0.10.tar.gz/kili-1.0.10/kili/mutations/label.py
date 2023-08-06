from ..helper import format_result, json_escape


def create_prediction(client, asset_id: str, json_response: str):
    result = client.execute('''
    mutation {
      createPrediction(
        assetID: "%s",
        jsonResponse: "%s") {
          id
          author {
            id
            email
          }
          labelType
          jsonResponse
          createdAt
          secondsToLabel
          totalSecondsToLabel
          honeypotMark
      }
    }
    ''' % (asset_id, json_escape(json_response)))
    return format_result('createPrediction', result)


def append_to_labels(client, author_id: str, json_response: str, label_asset_id: str, label_type: str, seconds_to_label: int, skipped: bool = False):
    result = client.execute('''
    mutation {
      appendToLabels(
        authorID: "%s",
        jsonResponse: "%s",
        labelAssetID: "%s",
        labelType: %s,
        secondsToLabel: %d,
        skipped: %s) {
          id
      }
    }
    ''' % (author_id, json_escape(json_response), label_asset_id, label_type, seconds_to_label, str(skipped).lower()))
    return format_result('appendToLabels', result)


def update_label(client, label_id: str, label_asset_id: str, review_asset_id: str, author_id: str, label_type: str, json_response: str, seconds_to_label: int):
    result = client.execute('''
    mutation {
      updateLabel(
        labelID: "%s",
        labelAssetID: "%s",
        reviewAssetID: "%s",
        authorID: "%s",
        labelType: %s,
        jsonResponse: "%s",
        secondsToLabel: %d) {
          id
      }
    }
    ''' % (label_id, label_asset_id, review_asset_id, author_id, label_type, json_escape(json_response), seconds_to_label))
    return format_result('updateLabel', result)


def update_properties_in_label(client, label_id: str, seconds_to_label: int = None, json_response: str = None):
    formatted_seconds_to_label = 'null' if seconds_to_label is None else f'{seconds_to_label}'
    formatted_json_response = 'null' if json_response is None else f'{json_response}'

    result = client.execute('''
        mutation {
          updatePropertiesInLabel(
            where: {id: "%s"},
            data: {
              secondsToLabel: %s
              jsonResponse: "%s"
            }
          ) {
            id
          }
        }
        ''' % (label_id, formatted_seconds_to_label, json_escape(json_response)))
    return format_result('updatePropertiesInLabel', result)
