{
  "type_id": "837300f3-b455-49a8-9141-d6b0444fbe5b",
  "type_alias": "TRUCK",
  "attributes": {
    "name": "truck_name"
  },
  "properties": {
    "P3_TRK_LSP_NAME": "lsp_name",
    "P3_TRK_TRUCK_REG":"truck_reg",
    "P3_TRK_TARE_MASS_KG": "tare_mass",
    "P3_TRK_SIZE":"truck_size",
    "P3_TRK_DRIVER_NAME":"driver_name",
    "XT_LSP_DRIVER_PP_NO":"passport_nr",
    "P3_TRK_DRIVER_LICENSE_NR":"licence_nr",
    "XT_LSP_DRIVER_CONTACT_NO":"driver_no",
    "P3_TRK_TARE_TIMESTAMP":"tare_timestamp",
    "TRUCK": "component_name",
  },
  "component_types": [
    {
      "type_id": "6215b5a1-86dc-4bd6-ae2b-e017ab9d8a4f",
      "type_alias": "bulk_lot",
      "attributes": {
        "name": "bulk_lot_id"
      },
    }
  ],
  "functions": {
    "now_time_utc_plus_2": "now_time",
    "pretty_format_timestamp": "format_timestamp",
    "round_number": "round"
  }
}