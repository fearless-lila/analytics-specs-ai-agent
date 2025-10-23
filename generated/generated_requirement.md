**DCSInteractionClick Event Requirements**

### 1. Event Name and BDD

* **Event Name**: `DCSInteractionClick`
* 
GIVEN I am viewing a DCS advert, carousel or stramp/tile  
WHEN I click / tap on the DCS item  
THEN Fire the `DCSInteractionClick` event


### 2. Fields

* basicOp
    + component = dcs
    + feature = various
    + isDeferred = true (note: deferred tracking change)
* [TrexDCS.interactions](../All/TrexDCS.md#Interactions)


### 3. Connectors - Adobe

#### Type: Combine

Combine the following fields into the trackState call:

| Adobe field | Bertie field | Note |
| --- | --- | --- |
| s.contextData['content_interaction'] = 1 | <basicOp.component>:`<basicOp.feature>` | |
| s.contextData['page_interaction_element_name']= | `<basicOp.component>` | |
| s.contextData['page_interaction_element_type']= | `<basicOp.component>` | |
| s.contextData['campaign_content']= | <`list1 and list2`> | see [List1 & List2](../../Connectors/Adobe/List2List1Syntax.md)|

As well as all other fields in [All Actions](../All/AllActions.md)