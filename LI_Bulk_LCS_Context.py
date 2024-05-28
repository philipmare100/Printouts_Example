{
  "type_id": "fd3d9774-ec93-403b-bab8-09b18ff9d367",
  "type_alias": "TRUCK",
  "attributes": {
    "name": "truck_name"
  },
  "properties": {
    "BUYER": "buyer",
    "TRUCK": "component_name",
    "LOTNUMBER": "lot_number",
    "XT_LSP_TRUCK_REG":"truck_reg",
    "XT_LSP_TRAIL_REG_1":"trailer_1_licence_nr",
    "XT_LSP_TRAIL_REG_2":"trailer_2_licence_nr",
    "MASSK_TRUCK_TARE_KG":"tare_mass",
    "MASSK_DATE_TIME_STAMP":"gross_timestamp",
    "XT_LSP_TRUCK_SIZE":"truck_size",
    "P3_TRK_TARE_TIMESTAMP":"tare_timestamp",
    "TRANSIT_PORT":"transit_port",
    "XT_LSP_NAME":"lsp_name",
    "XT_LSP_DRIVER_NAME":"driver_name",
    "XT_LSP_DRIVER_PP_NO":"passport_nr",
    "XT_LSP_DRIVER_LIC_NO":"licence_nr",
    "XT_LSP_DRIVER_CONTACT_NO":"driver_no"
  },
  "component_types": [
    {
      "type_id": "b39c55df-fb8f-4103-9d59-2ed87c0457c7",
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