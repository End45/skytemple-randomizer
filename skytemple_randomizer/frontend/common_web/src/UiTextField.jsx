/*
 * Copyright 2020-2023 Capypara and the SkyTemple Contributors
 *
 * This file is part of SkyTemple.
 *
 * SkyTemple is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * SkyTemple is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
 */

import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import React from "react";
import {useSettingsStyles} from "./theme";

export function UiTextField(props) {
    const classes = useSettingsStyles();
    return (
        <Paper className={classes.paper}>
            <TextField
                id={props.id}
                label={props.label}
                placeholder={props.label}
                defaultValue={props.initial}
                margin="none"
                multiline
                rows={24}
                onChange={(event) => props.onChange(props.id, event.target.value)}
            />
        </Paper>
    )
}