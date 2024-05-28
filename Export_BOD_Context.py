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
    "MASSK_TRUCK_GROSS_KG": "gross_mass",
    "P3_BAG_LOT_WB_NET_KG":"nett_mass",
    "P3_PUD_WB_VAR_PER":"mass_variance",
    "XT_LSP_TRUCK_SIZE":"truck_size",
    "P3_TRK_TARE_TIMESTAMP":"tare_timestamp",
    "MASSK_GROSS_TIMESTAMP":"gross_timestamp",
    "TRANSIT_PORT":"transit_port",
    "XT_LSP_NAME":"lsp_name",
    "XT_LSP_DRIVER_NAME":"driver_name",
    "XT_LSP_DRIVER_PP_NO":"passport_nr",
    "XT_LSP_DRIVER_LIC_NO":"licence_nr",
    "CONSIGNEE_2": "consignee_2",
    "CONSIGNEE_1": "consignee_1",
    "TRUCK_BAG_DESTINATION": "truck_bag_destination",
    "P3_BAG_LOT_INVOICE_MASS_KG": "bag_lot_invoice_mass",
    "TARP_SEAL": "tarp_seal"

  },
  "component_types": [
    {
      "type_id": "cf8a788f-2611-421e-825d-b99597ed360f",
      "type_alias": "bag_lot",
      "attributes": {
        "name": "bag_lot_id"
      },
    }
  ],
  "functions": {
    "now_time_utc_plus_2": "now_time",
    "pretty_format_timestamp": "format_timestamp",
    "round_number": "round",
    "get_drum_loc_in_list": "bag_index"
  }
}